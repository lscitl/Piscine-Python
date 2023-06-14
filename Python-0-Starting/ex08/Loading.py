#!/usr/bin/python3

"""
ft_tqdm(lst: range) -> None:

this function will display processing bar.
"""

import shutil
import time


def ft_tqdm(lst: range) -> None:
    column_space = shutil.get_terminal_size().columns
    total = len(lst)
    last_it_time = start_time = time.time()

    spit = 0
    spit_acc = 0

    for i in range(total):
        if i == 0:
            bar_str_s = "  0%|"
            bar_str_e = f"| 0/{total} [00:00<?, ?it/s]"
            bar_space = column_space - len(bar_str_s) - len(bar_str_e)
            if bar_space <= 0:
                bar = ""
            else:
                bar = " " * bar_space
            print("\r" + bar_str_s + bar + bar_str_e, end="", flush=True)
        else:
            cur_it_time = time.time()
            spit = cur_it_time - last_it_time
            last_it_time = cur_it_time
            spit_acc += spit

            if spit_acc > 0.1:
                spit_mean = (cur_it_time - start_time) / i

                elapsed_time = int(cur_it_time - start_time)
                elapsed_time_hour = elapsed_time // 3600
                elapsed_time_min = (elapsed_time % 3600) // 60
                elapsed_time_sec = elapsed_time % 60

                est_end_time = int((total - i) * spit_mean)
                est_end_time_hour = est_end_time // 3600
                est_end_time_min = (est_end_time % 3600) // 60
                est_end_time_sec = est_end_time % 60

                percentage = i / total * 100

                bar_str_s = f"{int(percentage):3}%|"
                bar_str_e = f"| {i}/{total} "

                if elapsed_time_hour:
                    bar_str_e += (
                        f"[{elapsed_time_hour:02}:{elapsed_time_min:02}"
                    )
                    bar_str_e += f":{elapsed_time_sec:02}<"
                else:
                    bar_str_e += (
                        f"[{elapsed_time_min:02}:{elapsed_time_sec:02}<"
                    )
                if est_end_time_hour:
                    bar_str_e += (
                        f"{est_end_time_hour:02}:{est_end_time_min:02}"
                    )
                    bar_str_e += f":{est_end_time_sec:02}, "
                else:
                    bar_str_e += (
                        f"{est_end_time_min:02}:{est_end_time_sec:02}, "
                    )
                if spit_mean < 1:
                    bar_str_e += f"{1/spit_mean:5.2f}it/s]"
                else:
                    bar_str_e += f"{spit_mean:5.2f}s/it]"

                bar_space = column_space - len(bar_str_s) - len(bar_str_e)
                if bar_space <= 0:
                    bar = ""
                else:
                    bar = int(percentage / 100 * bar_space) * "█"
                    bar += " " * (bar_space - len(bar))
                print("\r" + bar_str_s + bar + bar_str_e, end="", flush=True)
                spit_acc = 0

        yield

    else:
        cur_it_time = time.time()
        spit_mean = (cur_it_time - start_time) / total

        elapsed_time = int(cur_it_time - start_time)
        elapsed_time_hour = elapsed_time // 3600
        elapsed_time_min = (elapsed_time % 3600) // 60
        elapsed_time_sec = elapsed_time % 60

        bar_str_s = "100%|"
        bar_str_e = f"| {total}/{total} "
        if elapsed_time_hour:
            bar_str_e += f"[{elapsed_time_hour:02}:{elapsed_time_min:02}"
            bar_str_e += f":{elapsed_time_sec:02}"
        else:
            bar_str_e += f"[{elapsed_time_min:02}:{elapsed_time_sec:02}"
        bar_str_e += "<00:00, "
        if spit_mean < 1:
            bar_str_e += f"{1/spit_mean:5.2f}it/s]"
        else:
            bar_str_e += f"{spit_mean:5.2f}s/it]"

        bar_space = column_space - len(bar_str_s) - len(bar_str_e)
        bar = "█" * bar_space
        print("\r" + bar_str_s + bar + bar_str_e)


if __name__ == "__main__":
    print(__doc__)
