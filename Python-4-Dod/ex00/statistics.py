#!/usr/bin/python3

from typing import Any


def ft_mean(args: Any) -> float:
    """return mean values from given args."""
    if (
        len(args) == 0 or
        not all(map(lambda x: isinstance(x, (int, float)), args))
    ):
        raise ValueError("ERROR")
    return sum(args) / len(args)


def ft_median(args: Any) -> float:
    """return median value from given args."""
    if (
        len(args) == 0 or
        not all(map(lambda x: isinstance(x, (int, float)), args))
    ):
        raise ValueError("ERROR")
    elif len(args) == 1:
        return args[0]
    args = sorted(args)
    mid_idx = len(args) // 2 - 1
    if len(args) % 2 == 0:
        return (args[mid_idx] + args[mid_idx + 1]) / 2
    return args[len(args) // 2]


def ft_quartile(args: Any) -> list[float]:
    """return quartile values(25%, 75%) from given args."""
    if (
        len(args) < 2 or
        not all(map(lambda x: isinstance(x, (int, float)), args))
    ):
        raise ValueError("ERROR")
    ret = []
    args = sorted(args)

    # # using median value(Method 1)
    # if len(args) % 2 == 0:
    #     ret.append(ft_median(args[: len(args) // 2]))
    #     ret.append(ft_median(args[len(args) // 2:]))
    # else:
    #     ret.append(ft_median(args[: len(args) // 2]))
    #     ret.append(ft_median(args[len(args) // 2 + 1:]))

    # using median value and including it to half values(Method 2)
    if len(args) % 2 == 1:
        ret.append(ft_median(args[: len(args) // 2 + 1]))
    else:
        ret.append(ft_median(args[: len(args) // 2]))
    ret.append(ft_median(args[len(args) // 2:]))

    return list(map(float, ret))


def ft_std(args: Any) -> float:
    """return standard deviation value from given args."""
    if len(args) == 0:
        raise ValueError("ERROR")
    m = ft_mean(args)
    tmp = [(m - v) ** 2 for v in args]
    return (sum(tmp) / len(tmp)) ** 0.5


def ft_var(args: Any) -> float:
    """return variance value from given args."""
    if len(args) < 2:
        raise ValueError("ERROR")
    m = ft_mean(args)
    tmp = [(m - v) ** 2 for v in args]

    # # Bassel's correction is applied.
    # if len(args) == 1:
    #     raise ValueError("ERROR")
    # return sum(tmp) / (len(tmp) - 1)

    # Bassel's correction is not applied.
    return sum(tmp) / len(tmp)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """calculate the values from kwargs."""
    func = {
        "mean": ft_mean,
        "median": ft_median,
        "quartile": ft_quartile,
        "std": ft_std,
        "var": ft_var,
    }
    for v in kwargs.values():
        try:
            print(v, ":", func[v](args))

        except ValueError:
            print("ERROR")

        except Exception:
            pass


if __name__ == "__main__":
    print(ft_statistics.__doc__)
