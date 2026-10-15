"""
Crea en GitHub las etiquetas, los sprints (milestones) y una Issue por cada
historia de .github/backlog.json. Se puede correr varias veces: no duplica.

Lo ejecuta la acción «Crear backlog» (pestaña Actions → Crear backlog →
Run workflow). También genera docs/BACKLOG.md con:
    python .github/scripts/crear_backlog.py --markdown
"""
import json
import pathlib
import subprocess
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[2]
BACKLOG = json.loads((RAIZ / ".github/backlog.json").read_text(encoding="utf-8"))

COLORES = {
    "clientes": "1f77b4", "productos": "2ca02c", "facturacion": "d62728",
    "proveedores": "9467bd", "reportes": "ff7f0e",
}
NOMBRES = {
    "clientes": "Clientes", "productos": "Productos", "facturacion": "Facturación",
    "proveedores": "Proveedores", "reportes": "Reportes",
}


def cuerpo(h):
    criterios = "\n".join(f"- [ ] {c}" for c in h["criterios"])
    return (
        f"**Como** {h['como']}, **quiero** {h['quiero']}, **para** {h['para']}.\n\n"
        f"### Criterios de aceptación\n{criterios}\n\n"
        f"### Estimación\n"
        f"- Puntos (los pone el equipo en la planificación): \n"
        f"- Horas estimadas: \n"
        f"- Horas reales (al cerrar): \n\n"
        f"Módulo: `{h['modulo']}/` · Código: **{h['id']}**"
    )


def gh(*args, check=True):
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        print(r.stderr)
        sys.exit(r.returncode)
    return r.stdout


def crear_en_github():
    for modulo, color in COLORES.items():
        gh("label", "create", f"módulo:{modulo}", "--color", color, "--force")
    gh("label", "create", "historia", "--color", "0e8a16", "--force",
       "--description", "Historia de usuario del backlog")
    gh("label", "create", "pedido de cambio", "--color", "fbca04", "--force",
       "--description", "Cambio solicitado por el cliente durante el sprint")
    gh("label", "create", "impedimento", "--color", "b60205", "--force",
       "--description", "Algo que bloquea a un integrante")

    existentes = {m["title"] for m in json.loads(gh("api", "repos/{owner}/{repo}/milestones?state=all"))}
    for s in BACKLOG["sprints"]:
        if s["titulo"] not in existentes:
            gh("api", "repos/{owner}/{repo}/milestones", "-f", f"title={s['titulo']}",
               "-f", f"description={s['descripcion']}")

    ya = {i["title"] for i in json.loads(
        gh("issue", "list", "--state", "all", "--limit", "300", "--json", "title"))}
    creadas = 0
    for h in BACKLOG["historias"]:
        titulo = f"[{h['id']}] {h['titulo']}"
        if titulo in ya:
            continue
        gh("issue", "create", "--title", titulo, "--body", cuerpo(h),
           "--label", "historia", "--label", f"módulo:{h['modulo']}",
           "--milestone", f"Sprint {h['sprint']}")
        creadas += 1
        print("  +", titulo)
    print(f"Listo: {creadas} historias nuevas.")


def generar_markdown():
    lineas = [
        "# Product backlog — SoftQuijarro S.R.L.",
        "",
        "> Generado desde `.github/backlog.json`. En GitHub cada historia es una **Issue**",
        "> (pestaña *Issues*), agrupada por **Sprint** (milestone) y etiquetada por módulo.",
        "",
    ]
    for modulo, nombre in NOMBRES.items():
        lineas += [f"## {nombre} — carpeta `{modulo}/`", ""]
        for h in [x for x in BACKLOG["historias"] if x["modulo"] == modulo]:
            lineas += [
                f"### {h['id']} · {h['titulo']}  _(Sprint {h['sprint']})_",
                f"**Como** {h['como']}, **quiero** {h['quiero']}, **para** {h['para']}.",
                "",
                *[f"- [ ] {c}" for c in h["criterios"]],
                "",
            ]
    (RAIZ / "docs/BACKLOG.md").write_text("\n".join(lineas), encoding="utf-8")
    print("docs/BACKLOG.md generado")


if __name__ == "__main__":
    generar_markdown() if "--markdown" in sys.argv else crear_en_github()
