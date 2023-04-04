vi #!/usr/bin/python3
"""Display of a locked class."""


class LockedClass:
    """
    Only permit instatiation of attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
