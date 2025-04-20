import importlib.resources as pkg_resources


def read_text_resource(resource_name: str) -> str:
    """
    Read a text file from the package resources.

    Args:
        resource_name: Name of the resource file in the resources directory
                      (e.g., 'egan_orphanogenesis.txt')

    Returns:
        The contents of the file as a string, or None if the file is not found
    """
    with pkg_resources.open_text("agent_examples.resources", resource_name) as fp:
        return fp.read()
