from django import template

register = template.Library()


@register.filter(nome="remover_texto")
def remover(texto, r):
    return texto.replace(r, "")


@register.filter(name="verificardddpr")
def verificardddpr(telefone):
    ddd = telefone[0:4]
    if ddd == "(44)":
        return True
    else:
        return False


@register.filter(name="verificaruser")
def verificausuario(usuario, nome_do_grupo):
    if usuario.groups.filter(name=nome_do_grupo):
        return True
    else:
        return False

@register.filter(name="verificaplaca")
def verificaplaca(usuario, nome_do_grupo):
    if usuario.groups.filter(name=nome_do_grupo):
        return True
    else:
        return False
