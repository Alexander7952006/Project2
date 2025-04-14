from API import geometrical_operations as gp
import functools

def dec_tr_translate(space_param):
    """Декоратор на основе функции tr_translate.

    Args:
        space_param(int or float): отступ параллельно перенесенной последовательности
         от исходных значений

    Returns:
        decorator(function): задекорировання функция
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            new_args = list(args)
            new_args[0] =  gp.tr_translate(new_args[0], space = space_param)
            result = func(*new_args)
            return result
        return wrapper
    return decorator


def dec_tr_rotate(angle):
    """Декоратор на основе функции tr_rotate.

        Args:
            angle(int or float): угол поворота последовательности

        Returns:
            decorator(function): задекорировання функция
        """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            new_args = list(args)
            new_args[0] =  gp.tr_rotate(new_args[0], degrees = angle)
            result = func(*new_args)
            return result
        return wrapper
    return decorator


def dec_tr_symmetry(space_param):
    """Декоратор на основе функции tr_symmetry.

        Args:
            space_param(int or float): отступ симметрично перенесенной последовательности
             от исходных значений

        Returns:
            decorator(function): задекорировання функция
        """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            new_args = list(args)
            new_args[0] =  gp.tr_symmetry(new_args[0], space = space_param)
            result = func(*new_args)
            return result
        return wrapper
    return decorator


def dec_tr_homothety(k, space_param):
    """Декоратор на основе функции tr_homothety.

        Args:
            space_param(int or float): отступ подобной последовательности
             от исходных значений
            k(int or float): коефицент подобия

        Returns:
            decorator(function): задекорировання функция
        """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            new_args = list(args)
            new_args[0] =  gp.tr_homothety(new_args[0], k = k, space = space_param)
            result = func(*new_args)
            return result
        return wrapper
    return decorator

