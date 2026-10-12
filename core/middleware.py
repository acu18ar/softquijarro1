from django.contrib.auth.views import redirect_to_login

RUTAS_PUBLICAS = ("/ingresar/", "/admin/", "/static/", "/salud/")


class LoginObligatorioMiddleware:
    """Todo el sistema exige iniciar sesión, salvo el login, el admin y /salud/.

    Así ningún estudiante tiene que acordarse de proteger sus vistas.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and not request.path.startswith(
            RUTAS_PUBLICAS
        ):
            return redirect_to_login(request.get_full_path())
        return self.get_response(request)
