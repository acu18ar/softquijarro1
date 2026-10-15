"""
Verifica que cada estudiante solo modifique archivos de SU carpeta.

Uso (lo ejecuta GitHub Actions en cada pull request):
    python verificar_carpeta.py <ruta/equipo.json> <usuario_github> < archivos_cambiados.txt
"""
import json
import sys


def verificar(equipo, autor, archivos):
    """Devuelve (ok, mensajes)."""
    autor_min = autor.lower()
    if autor_min == equipo.get("docente", "").lower():
        return True, [f"👨‍🏫 {autor} es el docente: puede modificar cualquier archivo."]

    estudiantes = {u.lower(): c for u, c in equipo.get("estudiantes", {}).items()}
    if autor_min not in estudiantes:
        return False, [
            f"❌ El usuario '{autor}' no está registrado en .github/equipo.json.",
            "   Pide al docente que te agregue con tu carpeta.",
        ]

    carpetas = estudiantes[autor_min]
    if isinstance(carpetas, str):
        carpetas = [carpetas]
    prefijos = tuple(c.strip("/") + "/" for c in carpetas)
    fuera = [a for a in archivos if not a.startswith(prefijos)]

    if fuera:
        return False, [
            f"❌ {autor}, tu carpeta es: {', '.join(carpetas)}",
            "   Pero este pull request modifica archivos de otros:",
            *[f"     - {a}" for a in fuera],
            "",
            "   Cómo arreglarlo: deshaz esos cambios en tu rama",
            "   (git checkout origin/main -- <archivo>), haz commit y push.",
            "   Si de verdad necesitas cambiar algo compartido, ábrelo como Issue",
            "   para que lo haga el docente.",
        ]
    return True, [f"✅ {autor}: todos los cambios están dentro de {', '.join(carpetas)}."]


def main():
    ruta_equipo, autor = sys.argv[1], sys.argv[2]
    with open(ruta_equipo, encoding="utf-8") as f:
        equipo = json.load(f)
    archivos = [linea.strip() for linea in sys.stdin if linea.strip()]
    ok, mensajes = verificar(equipo, autor, archivos)
    print("\n".join(mensajes))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
