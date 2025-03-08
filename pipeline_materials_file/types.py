"""Materials pipe types stuff."""


class PipeType:
    """Weld type_id field values."""

    DIRECT = 0
    SPIRAL = 1
    EMPTY = 2


def float2str(val, decimal=2):
    """Format float as string."""
    if val is None:
        return ''
    mask = "%0.0" + str(decimal) + "f"
    ret = mask % val
    return ret.replace('.', ',')


def str2float(text):
    """Restore float from string."""
    return float(text.replace(',', '.'))
