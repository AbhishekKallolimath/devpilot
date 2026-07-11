import platform


def get_os():
    return f"{platform.system()} {platform.release()}"