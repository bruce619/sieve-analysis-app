import tkinter as tk
from tkinter import ttk, Menu, scrolledtext, messagebox, END
import numpy as np
import matplotlib.pyplot as plt
from backend import *


window = tk.Tk()
window.title("GRAIN SIZE DISTRIBUTION ANALYSIS APP")
window.iconbitmap("Sieve-Analysis.ico")
window.minsize(760, 500)
window.resizable(False, False)


def cal_wt_retained():
    col_one = [emp_sieve_one_entry.get(), emp_sieve_two_entry.get(), emp_sieve_three_entry.get(), emp_sieve_four_entry.get(),
               emp_sieve_five_entry.get(), emp_sieve_six_entry.get(), emp_sieve_seven_entry.get(), bottom_pan_entry.get()]

    col_two = [sieve_samp_weight_one_entry.get(), sieve_samp_weight_two_entry.get(), sieve_samp_weight_three_entry.get(),
               sieve_samp_weight_four_entry.get(), sieve_samp_weight_five_entry.get(), sieve_samp_weight_six_entry.get(),
               sieve_samp_weight_seven_entry.get(), sieve_samp_weight_bottom_pan_entry.get()]

    result_col = [retained_samp_weight_one_entry, retained_samp_weight_two_entry, retained_samp_weight_three_entry,
                  retained_samp_weight_four_entry, retained_samp_weight_five_entry, retained_samp_weight_six_entry,
                  retained_samp_weight_seven_entry, retained_samp_weight_bottom_pan_entry]
    count = 0
    while count < len(col_one) and count < len(col_two):
        try:
            num1 = float(col_one[count])
            num2 = float(col_two[count])
            wt_of_sam_ret_result = wt_of_sam_ret(num1, num2)
            result_col[count].delete(0, END)
            result_col[count].insert(END, wt_of_sam_ret_result)
            count += 1
        except ValueError:
            messagebox.showerror("Invalid Value Input", "Kindly use values in decimal format e.g 234.68")
            break
        except TypeError:
            messagebox.showerror("Invalid Value Type", "must be number not string or none")
            break

    result_col_get = [retained_samp_weight_one_entry.get(), retained_samp_weight_two_entry.get(),
                      retained_samp_weight_three_entry.get(), retained_samp_weight_four_entry.get(),
                      retained_samp_weight_five_entry.get(), retained_samp_weight_six_entry.get(),
                      retained_samp_weight_seven_entry.get(), retained_samp_weight_bottom_pan_entry.get()]

    # sum up the weight of sample retained rows rows
    result_col_get_float = sum([float(i) for i in result_col_get])

    total_samp_weight_retained_entry.delete(0, END)
    total_samp_weight_retained_entry.insert(END, "{0:.2f}".format(result_col_get_float))
    return result_col_get_float


def cal_cor_wt_retained():
    rt_smp_wt_col = [retained_samp_weight_one_entry.get(), retained_samp_weight_two_entry.get(),
                     retained_samp_weight_three_entry.get(), retained_samp_weight_four_entry.get(),
                     retained_samp_weight_five_entry.get(), retained_samp_weight_six_entry.get(),
                     retained_samp_weight_seven_entry.get(), retained_samp_weight_bottom_pan_entry.get()]

    col_one = [float(i) for i in rt_smp_wt_col]

    result_col = [corrected_samp_weight_one_entry, corrected_samp_weight_two_entry, corrected_samp_weight_three_entry,
                  corrected_samp_weight_four_entry, corrected_samp_weight_five_entry, corrected_samp_weight_six_entry,
                  corrected_samp_weight_seven_entry, corrected_samp_weight_bottom_pan_entry]

    count = 0
    while count < len(col_one):
        try:
            num1 = float(initial_weight_of_sample_entry.get())
            num2 = float("{0:.2f}".format(cal_wt_retained()))
            cor_wt_of_sam_ret_result = cor_wt_sam_ret(num1, num2)
            ans = col_one[count] + cor_wt_of_sam_ret_result
            result_col[count].delete(0, END)
            result_col[count].insert(END, "{0:.3f}".format(ans))
            count += 1
        except ValueError:
            messagebox.showerror("Invalid Value Input", "Kindly use values in decimal format e.g 234.68")
            break
        except TypeError:
            messagebox.showerror("Invalid Value Type", "must be number not string or none")
            break


def cal_percent_wt_retained():
    cor_wt_smp_rt = [corrected_samp_weight_one_entry.get(), corrected_samp_weight_two_entry.get(),
                     corrected_samp_weight_three_entry.get(), corrected_samp_weight_four_entry.get(),
                     corrected_samp_weight_five_entry.get(), corrected_samp_weight_six_entry.get(),
                     corrected_samp_weight_seven_entry.get(), corrected_samp_weight_bottom_pan_entry.get()]

    result_col = [percentage_weight_one_entry, percentage_weight_two_entry, percentage_weight_three_entry,
                  percentage_weight_four_entry, percentage_weight_five_entry, percentage_weight_six_entry,
                  percentage_weight_seven_entry, percentage_weight_bottom_pan_entry]

    col_one = [float(i) for i in cor_wt_smp_rt]

    count = 0
    while count < len(cor_wt_smp_rt):
        try:
            num1 = float(col_one[count])
            num2 = float(initial_weight_of_sample_entry.get())
            ans = percent_wt_ret(num1, num2)
            result_col[count].delete(0, END)
            result_col[count].insert(END, "{0:.2f}".format(ans))
            count += 1
        except ValueError:
            messagebox.showerror("Invalid Value Input", "Kindly use values in decimal format e.g 234.68")
            break
        except TypeError:
            messagebox.showerror("Invalid Value Type", "must be number not string or none")
            break


def cal_cumulative_percent_wt_retained():
    percent_wt = [percentage_weight_one_entry.get(), percentage_weight_two_entry.get(), percentage_weight_three_entry.get(),
                  percentage_weight_four_entry.get(), percentage_weight_five_entry.get(), percentage_weight_six_entry.get(),
                  percentage_weight_seven_entry.get(), percentage_weight_bottom_pan_entry.get()]

    result_col = [cumulative_percentage_weight_one_entry, cumulative_percentage_weight_two_entry,
                  cumulative_percentage_weight_three_entry, cumulative_percentage_weight_four_entry,
                  cumulative_percentage_weight_five_entry, cumulative_percentage_weight_six_entry,
                  cumulative_percentage_weight_seven_entry, cumulative_percentage_weight_bottom_pan_entry]

    col_one = [float(i) for i in percent_wt]
    count = 0
    count_two = 1
    while count < len(col_one) and count_two < len(result_col):
        try:
            result_col[0].delete(0, END)
            result_col[0].insert(END, "{0:.2f}".format(col_one[0]))
            unsaved_col = [cumulative_percentage_weight_one_entry.get(), cumulative_percentage_weight_two_entry.get(),
                           cumulative_percentage_weight_three_entry.get(), cumulative_percentage_weight_four_entry.get(),
                           cumulative_percentage_weight_five_entry.get(), cumulative_percentage_weight_six_entry.get(),
                           cumulative_percentage_weight_seven_entry.get(), cumulative_percentage_weight_bottom_pan_entry.get()]
            col_two = [float(i) for i in unsaved_col]

            ans = cu_pt_wt_rt(col_two[count], col_one[count_two])
            result_col[count_two].delete(0, END)
            result_col[count_two].insert(END, "{0:.2f}".format(ans))
            count += 1
            count_two += 1
        except ValueError:
            messagebox.showerror("Invalid Value Input", "Kindly use values in decimal format e.g 234.68")
            break
        except TypeError:
            messagebox.showerror("Invalid Value Type", "must be number not string or none")
            break


def cal_percent_wt_finer():
    cu_pt_wt_ent = [cumulative_percentage_weight_one_entry.get(), cumulative_percentage_weight_two_entry.get(),
                    cumulative_percentage_weight_three_entry.get(), cumulative_percentage_weight_four_entry.get(),
                    cumulative_percentage_weight_five_entry.get(), cumulative_percentage_weight_six_entry.get(),
                    cumulative_percentage_weight_seven_entry.get(), cumulative_percentage_weight_bottom_pan_entry.get()]

    result_col = [percentage_weight_finer_one_entry, percentage_weight_finer_two_entry,
                  percentage_weight_finer_three_entry, percentage_weight_finer_four_entry,
                  percentage_weight_finer_five_entry, percentage_weight_finer_six_entry,
                  percentage_weight_finer_seven_entry, percentage_weight_finer_bottom_pan_entry]

    col_one = [float(i) for i in cu_pt_wt_ent]

    count = 0

    while count < len(col_one):
        try:
            result_col[count].delete(0, END)
            ans = pt_finer(col_one[count])
            result_col[count].insert(END, "{0:.2f}".format(ans))
            rows = [percentage_weight_finer_one_entry.get(), percentage_weight_finer_two_entry.get(),
                    percentage_weight_finer_three_entry.get(), percentage_weight_finer_four_entry.get(),
                    percentage_weight_finer_five_entry.get(), percentage_weight_finer_six_entry.get(),
                    percentage_weight_finer_seven_entry.get(), percentage_weight_finer_bottom_pan_entry.get()]
            float_rows = [float(i) for i in rows]
            if float_rows[count] > 100.0 or float_rows[count] < 0.00:
                messagebox.showerror("Error in %Wt Finer", "Values must be within 100.0 and 0.00.\
                                        \nMake sure there are no negative values or values greater than 100.0")
                break
            count += 1
        except ValueError:
            messagebox.showerror("Invalid Value Input", "Kindly use values in decimal format e.g 234.68")
            break
        except TypeError:
            messagebox.showerror("Invalid Value Type", "must be number not string or none")
            break


def new_window():
    tk.Toplevel(window)


def do_nothing():
    pass


def do_something():
    pass


def grain_size_plot():
    rows = [percentage_weight_finer_one_entry.get(), percentage_weight_finer_two_entry.get(),
            percentage_weight_finer_three_entry.get(), percentage_weight_finer_four_entry.get(),
            percentage_weight_finer_five_entry.get(), percentage_weight_finer_six_entry.get(),
            percentage_weight_finer_seven_entry.get()]

    y = [float(i) for i in rows]
    x = [2.8000, 1.8000, 0.6000, 0.4250, 0.250, 0.1250, 0.0053]
    fig, ax = plt.subplots()
    ax.plot(x, y, color="green", marker='o', markerfacecolor='red')
    ax.set(xlabel='Particle Diameter (mm)', ylabel='Percentage Finer (%)',
           title='Grain Size Distribution curve')
    ax.set_ylim(0.00, 100.00)
    ax.set_xlim(0.001, 100)
    ax.set_xscale('log')
    ax.grid(True)
    fig.savefig("test.png")
    plt.show(block=False)


def uniformity_coefficient():
    rows = [percentage_weight_finer_one_entry.get(), percentage_weight_finer_two_entry.get(),
            percentage_weight_finer_three_entry.get(), percentage_weight_finer_four_entry.get(),
            percentage_weight_finer_five_entry.get(), percentage_weight_finer_six_entry.get(),
            percentage_weight_finer_seven_entry.get()]

    y = [float(i) for i in rows]
    x = [2.8000, 1.8000, 0.6000, 0.4250, 0.250, 0.1250, 0.0053]
    fig, ax = plt.subplots()
    ax.plot(x, y, color="green", marker='o', markerfacecolor='red')
    ax.set(xlabel='Particle Diameter (mm)', ylabel='Percentage Finer (%)',
           title='Grain Size Distribution Curve with Uniformity Coefficient (Cu)')
    ymin = 0
    xmin = 0.001

    y1, y2 = 10, 60
    x1, x2 = np.exp(np.interp([y1, y2], y[::-1], np.log(x[::-1])))

    values = []

    for xi, yi in [(x1, y1), (x2, y2)]:
        ax.hlines(yi, xmin, xi, color='r')
        ax.vlines(xi, ymin, yi, color='r')
        values.append(xi)

    points = [float(i) for i in values]
    Cu = float("{0:.3}".format(points[1]/points[0]))

    if 1.00 <= Cu < 4.00:
        interpretation_box.insert(END, "The Uniformity Coefficient is {}, which means the soil is poorly/uniformly graded".format(Cu))
    elif 4.00 <= Cu < 6.00:
        interpretation_box.insert(END, "The Uniformity Coefficient is {}, which means the soil is well graded gravel".format(Cu))
    elif Cu > 6.00:
        interpretation_box.insert(END,
                                  "The Uniformity Coefficient is {}, which means the soil is well graded sand".format(
                                      Cu))

    ax.set_ylim(ymin, 100)
    ax.set_xlim(xmin, 100)
    ax.set_xscale('log')
    ax.grid(True)
    plt.show(block=False)


def help_message():
    messagebox.showinfo("How To Perform Test", "")


def about_message():
    messagebox.showinfo("Grain Size Analysis App", "Typical laboratory test conducted in the soil mechanics field.\
    The purpose of the analysis is to derive the particle size distribution of soils.")


menu_bar = Menu(window)
window.config(menu=menu_bar)

filemenu = Menu(menu_bar, tearoff=0)
filemenu.add_command(label="New", command=new_window)
filemenu.add_command(label="Open", command=do_nothing)
filemenu.add_command(label="Save", command=do_nothing)
filemenu.add_command(label="Save as...", command=do_nothing)
filemenu.add_command(label="Close", command=do_nothing)
filemenu.add_separator()
filemenu.add_command(label="Print", command=do_nothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menu_bar, tearoff=0)
editmenu.add_command(label="Undo", command=do_something)
editmenu.add_command(label="Redo", command=do_something)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=do_something)
editmenu.add_command(label="Copy", command=do_something)
editmenu.add_command(label="Paste", command=do_something)
editmenu.add_command(label="Delete", command=do_something)
menu_bar.add_cascade(label="Edit", menu=editmenu)

plotmenu = Menu(menu_bar, tearoff=0)
plotmenu.add_command(label="Grain Size Distribution Curve", command=grain_size_plot)
plotmenu.add_separator()
plotmenu.add_command(label="Uniformity Coefficient (CU)", command=uniformity_coefficient)
menu_bar.add_cascade(label="Plot", menu=plotmenu)

helpmenu = Menu(menu_bar, tearoff=0)
helpmenu.add_command(label="Help Index", command=help_message)
helpmenu.add_command(label="About...", command=about_message)
menu_bar.add_cascade(label="Help", menu=helpmenu)


# first Column "Sieve Size"

sieve_size_col = ttk.Label(window, text="Sieve Size")
sieve_size_col.grid(column=0, row=0)

sieve_one = ttk.Label(window, text="2.8mm")
sieve_one.grid(column=0, row=1)

sieve_two = ttk.Label(window, text="1.8mm")
sieve_two.grid(column=0, row=2)

sieve_three = ttk.Label(window, text="600um")
sieve_three.grid(column=0, row=3)

sieve_four= ttk.Label(window, text="425um")
sieve_four.grid(column=0, row=4)

sieve_five = ttk.Label(window, text="250um")
sieve_five.grid(column=0, row=5)

sieve_six = ttk.Label(window, text="125um")
sieve_six.grid(column=0, row=6)

sieve_seven = ttk.Label(window, text="53mic")
sieve_seven.grid(column=0, row=7)

sieve_pan = ttk.Label(window, text=" Bottom Pan")
sieve_pan.grid(column=0, row=8)

initial_weight_of_sample_col = ttk.Label(window, text="Measured Sample\nWeight (g)")
initial_weight_of_sample_col.grid(column=0, row=10)


# Second Column "Weight of empty sieve"

emp_sieve_weight_col = ttk.Label(window, text="Weight of Empty\nsieve")
emp_sieve_weight_col.grid(column=1, row=0)

emp_sieve_one = tk.DoubleVar()
emp_sieve_one_entry = ttk.Entry(window, width=13, textvariable=emp_sieve_one)
emp_sieve_one_entry.grid(column=1, row=1)

emp_sieve_two = tk.DoubleVar()
emp_sieve_two_entry = ttk.Entry(window, width=13, textvariable=emp_sieve_two)
emp_sieve_two_entry.grid(column=1, row=2)

emp_sieve_three = tk.DoubleVar()
emp_sieve_three_entry = ttk.Entry(window, width=13, textvariable=emp_sieve_three)
emp_sieve_three_entry.grid(column=1, row=3)

emp_sieve_four = tk.DoubleVar()
emp_sieve_four_entry = ttk.Entry(window, width=13, textvariable=emp_sieve_four)
emp_sieve_four_entry.grid(column=1, row=4)

emp_sieve_five = tk.DoubleVar()
emp_sieve_five_entry = ttk.Entry(window, width=13, textvariable=emp_sieve_five)
emp_sieve_five_entry.grid(column=1, row=5)

emp_sieve_six = tk.DoubleVar()
emp_sieve_six_entry = ttk.Entry(window, width=13, textvariable=emp_sieve_six)
emp_sieve_six_entry.grid(column=1, row=6)

emp_sieve_seven = tk.DoubleVar()
emp_sieve_seven_entry = ttk.Entry(window, width=13, textvariable=emp_sieve_seven)
emp_sieve_seven_entry.grid(column=1, row=7)

bottom_pan = tk.DoubleVar()
bottom_pan_entry = ttk.Entry(window, width=13, textvariable=bottom_pan)
bottom_pan_entry.grid(column=1, row=8)

initial_weight_of_sample = tk.DoubleVar()
initial_weight_of_sample_entry = ttk.Entry(window, width=13, textvariable=initial_weight_of_sample)
initial_weight_of_sample_entry.grid(column=1, row=10)
initial_weight_of_sample.set(500.00)

# Third Column " Weight of Sieve + Sample"

sieve_samp_weight_col = ttk.Label(window, text="Weight of\nSieve + Sample")
sieve_samp_weight_col.grid(column=2, row=0)

sieve_samp_weight_one = tk.DoubleVar()
sieve_samp_weight_one_entry = ttk.Entry(window, width=13, textvariable=sieve_samp_weight_one)
sieve_samp_weight_one_entry.grid(column=2, row=1)

sieve_samp_weight_two = tk.DoubleVar()
sieve_samp_weight_two_entry = ttk.Entry(window, width=13, textvariable=sieve_samp_weight_two)
sieve_samp_weight_two_entry.grid(column=2, row=2)

sieve_samp_weight_three = tk.DoubleVar()
sieve_samp_weight_three_entry = ttk.Entry(window, width=13, textvariable=sieve_samp_weight_three)
sieve_samp_weight_three_entry.grid(column=2, row=3)

sieve_samp_weight_four = tk.DoubleVar()
sieve_samp_weight_four_entry = ttk.Entry(window, width=13, textvariable=sieve_samp_weight_four)
sieve_samp_weight_four_entry.grid(column=2, row=4)

sieve_samp_weight_five = tk.DoubleVar()
sieve_samp_weight_five_entry = ttk.Entry(window, width=13, textvariable=sieve_samp_weight_five)
sieve_samp_weight_five_entry.grid(column=2, row=5)

sieve_samp_weight_six = tk.DoubleVar()
sieve_samp_weight_six_entry = ttk.Entry(window, width=13, textvariable=sieve_samp_weight_six)
sieve_samp_weight_six_entry.grid(column=2, row=6)

sieve_samp_weight_seven = tk.DoubleVar()
sieve_samp_weight_seven_entry = ttk.Entry(window, width=13, textvariable=sieve_samp_weight_seven)
sieve_samp_weight_seven_entry.grid(column=2, row=7)

sieve_samp_weight_bottom_pan = tk.DoubleVar()
sieve_samp_weight_bottom_pan_entry = ttk.Entry(window, width=13, textvariable=sieve_samp_weight_bottom_pan)
sieve_samp_weight_bottom_pan_entry.grid(column=2, row=8)

total_wt_retained_label = ttk.Label(window, text="Total Weight =")
total_wt_retained_label.grid(column=2, row=9)

# Fourth Column "Weight of Sample retained"

retained_samp_weight_col = ttk.Label(window, text="Weight of\nSample Retained")
retained_samp_weight_col.grid(column=3, row=0)

retained_samp_weight_one = tk.DoubleVar()
retained_samp_weight_one_entry = ttk.Entry(window, width=13, textvariable=retained_samp_weight_one)
retained_samp_weight_one_entry.grid(column=3, row=1)


retained_samp_weight_two = tk.DoubleVar()
retained_samp_weight_two_entry = ttk.Entry(window, width=13, textvariable=retained_samp_weight_two)
retained_samp_weight_two_entry.grid(column=3, row=2)

retained_samp_weight_three = tk.DoubleVar()
retained_samp_weight_three_entry = ttk.Entry(window, width=13, textvariable=retained_samp_weight_three)
retained_samp_weight_three_entry.grid(column=3, row=3)


retained_samp_weight_four = tk.DoubleVar()
retained_samp_weight_four_entry = ttk.Entry(window, width=13, textvariable=retained_samp_weight_four)
retained_samp_weight_four_entry.grid(column=3, row=4)


retained_samp_weight_five = tk.DoubleVar()
retained_samp_weight_five_entry = ttk.Entry(window, width=13, textvariable=retained_samp_weight_five)
retained_samp_weight_five_entry.grid(column=3, row=5)

retained_samp_weight_six = tk.DoubleVar()
retained_samp_weight_six_entry = ttk.Entry(window, width=13, textvariable=retained_samp_weight_six)
retained_samp_weight_six_entry.grid(column=3, row=6)

retained_samp_weight_seven = tk.DoubleVar()
retained_samp_weight_seven_entry = ttk.Entry(window, width=13, textvariable=retained_samp_weight_seven)
retained_samp_weight_seven_entry.grid(column=3, row=7)

retained_samp_weight_bottom_pan = tk.DoubleVar()
retained_samp_weight_bottom_pan_entry = ttk.Entry(window, width=13, textvariable=retained_samp_weight_bottom_pan)
retained_samp_weight_bottom_pan_entry.grid(column=3, row=8)


total_samp_weight_retained = tk.DoubleVar()
total_samp_weight_retained_entry = ttk.Entry(window, width=13, textvariable=total_samp_weight_retained)
total_samp_weight_retained_entry.grid(column=3, row=9)


wt_retained = ttk.Button(window, text="Calculate", command=cal_wt_retained)
wt_retained.grid(column=3, row=10)


# Fifth Column "Corrected Weight of Sample retained"

corrected_samp_weight_col = ttk.Label(window, text="Corrected Weight of\nSample Retained")
corrected_samp_weight_col.grid(column=4, row=0)

corrected_samp_weight_one = tk.DoubleVar()
corrected_samp_weight_one_entry = ttk.Entry(window, width=13, textvariable=corrected_samp_weight_one)
corrected_samp_weight_one_entry.grid(column=4, row=1)

corrected_samp_weight_two = tk.DoubleVar()
corrected_samp_weight_two_entry = ttk.Entry(window, width=13, textvariable=corrected_samp_weight_two)
corrected_samp_weight_two_entry.grid(column=4, row=2)

corrected_samp_weight_three = tk.DoubleVar()
corrected_samp_weight_three_entry = ttk.Entry(window, width=13, textvariable=corrected_samp_weight_three)
corrected_samp_weight_three_entry.grid(column=4, row=3)

corrected_samp_weight_four = tk.DoubleVar()
corrected_samp_weight_four_entry = ttk.Entry(window, width=13, textvariable=corrected_samp_weight_four)
corrected_samp_weight_four_entry.grid(column=4, row=4)

corrected_samp_weight_five = tk.DoubleVar()
corrected_samp_weight_five_entry = ttk.Entry(window, width=13, textvariable=corrected_samp_weight_five)
corrected_samp_weight_five_entry.grid(column=4, row=5)

corrected_samp_weight_six = tk.DoubleVar()
corrected_samp_weight_six_entry = ttk.Entry(window, width=13, textvariable=corrected_samp_weight_six)
corrected_samp_weight_six_entry.grid(column=4, row=6)

corrected_samp_weight_seven = tk.DoubleVar()
corrected_samp_weight_seven_entry = ttk.Entry(window, width=13, textvariable=corrected_samp_weight_seven)
corrected_samp_weight_seven_entry.grid(column=4, row=7)

corrected_samp_weight_bottom_pan = tk.DoubleVar()
corrected_samp_weight_bottom_pan_entry = ttk.Entry(window, width=13, textvariable=corrected_samp_weight_bottom_pan)
corrected_samp_weight_bottom_pan_entry.grid(column=4, row=8)

cor_wt_retained = ttk.Button(window, text="Calculate", command=cal_cor_wt_retained)
cor_wt_retained.grid(column=4, row=9)

# Six Column "Corrected Weight of Sample retained"

percentage_weight_col = ttk.Label(window, text="% Weight\nRetained")
percentage_weight_col.grid(column=5, row=0)

percentage_weight_one = tk.DoubleVar()
percentage_weight_one_entry = ttk.Entry(window, width=13, textvariable=percentage_weight_one)
percentage_weight_one_entry.grid(column=5, row=1)

percentage_weight_two = tk.DoubleVar()
percentage_weight_two_entry = ttk.Entry(window, width=13, textvariable=percentage_weight_two)
percentage_weight_two_entry.grid(column=5, row=2)

percentage_weight_three = tk.DoubleVar()
percentage_weight_three_entry = ttk.Entry(window, width=13, textvariable=percentage_weight_three)
percentage_weight_three_entry.grid(column=5, row=3)

percentage_weight_four = tk.DoubleVar()
percentage_weight_four_entry = ttk.Entry(window, width=13, textvariable=percentage_weight_four)
percentage_weight_four_entry.grid(column=5, row=4)

percentage_weight_five = tk.DoubleVar()
percentage_weight_five_entry = ttk.Entry(window, width=13, textvariable=percentage_weight_five)
percentage_weight_five_entry.grid(column=5, row=5)

percentage_weight_six = tk.DoubleVar()
percentage_weight_six_entry = ttk.Entry(window, width=13, textvariable=percentage_weight_six)
percentage_weight_six_entry.grid(column=5, row=6)

percentage_weight_seven = tk.DoubleVar()
percentage_weight_seven_entry = ttk.Entry(window, width=13, textvariable=percentage_weight_seven)
percentage_weight_seven_entry.grid(column=5, row=7)

percentage_weight_bottom_pan = tk.DoubleVar()
percentage_weight_bottom_pan_entry = ttk.Entry(window, width=13, textvariable=percentage_weight_bottom_pan)
percentage_weight_bottom_pan_entry.grid(column=5, row=8)

percent_wt_retained = ttk.Button(window, text="Calculate", command=cal_percent_wt_retained)
percent_wt_retained.grid(column=5, row=9)


# Seventh Column "Corrected Weight of Sample retained"

cumulative_percentage_weight_col = ttk.Label(window, text="Cumulative %\nWeight Retained")
cumulative_percentage_weight_col.grid(column=6, row=0)

cumulative_percentage_weight_one = tk.DoubleVar()
cumulative_percentage_weight_one_entry = ttk.Entry(window, width=13, textvariable=cumulative_percentage_weight_one)
cumulative_percentage_weight_one_entry.grid(column=6, row=1)

cumulative_percentage_weight_two = tk.DoubleVar()
cumulative_percentage_weight_two_entry = ttk.Entry(window, width=13, textvariable=cumulative_percentage_weight_two)
cumulative_percentage_weight_two_entry.grid(column=6, row=2)

cumulative_percentage_weight_three = tk.DoubleVar()
cumulative_percentage_weight_three_entry = ttk.Entry(window, width=13, textvariable=cumulative_percentage_weight_three)
cumulative_percentage_weight_three_entry.grid(column=6, row=3)

cumulative_percentage_weight_four = tk.DoubleVar()
cumulative_percentage_weight_four_entry = ttk.Entry(window, width=13, textvariable=cumulative_percentage_weight_four)
cumulative_percentage_weight_four_entry.grid(column=6, row=4)

cumulative_percentage_weight_five = tk.DoubleVar()
cumulative_percentage_weight_five_entry = ttk.Entry(window, width=13, textvariable=cumulative_percentage_weight_five)
cumulative_percentage_weight_five_entry.grid(column=6, row=5)

cumulative_percentage_weight_six = tk.DoubleVar()
cumulative_percentage_weight_six_entry = ttk.Entry(window, width=13, textvariable=cumulative_percentage_weight_six)
cumulative_percentage_weight_six_entry.grid(column=6, row=6)

cumulative_percentage_weight_seven = tk.DoubleVar()
cumulative_percentage_weight_seven_entry = ttk.Entry(window, width=13, textvariable=cumulative_percentage_weight_seven)
cumulative_percentage_weight_seven_entry.grid(column=6, row=7)

cumulative_percentage_weight_bottom_pan = tk.DoubleVar()
cumulative_percentage_weight_bottom_pan_entry = ttk.Entry(window, width=13, textvariable=cumulative_percentage_weight_bottom_pan)
cumulative_percentage_weight_bottom_pan_entry.grid(column=6, row=8)

cumulative_percent_wt_retained = ttk.Button(window, text="Calculate", command=cal_cumulative_percent_wt_retained)
cumulative_percent_wt_retained.grid(column=6, row=9)

# Eight Column "Percentage Weight Finer"

percentage_weight_finer_col = ttk.Label(window, text="% Weight\nFiner")
percentage_weight_finer_col.grid(column=7, row=0)

percentage_weight_finer_one = tk.DoubleVar()
percentage_weight_finer_one_entry = ttk.Entry(window, width=13, textvariable=percentage_weight_finer_one)
percentage_weight_finer_one_entry.grid(column=7, row=1)

percentage_weight_finer_two = tk.DoubleVar()
percentage_weight_finer_two_entry = ttk.Entry(window, width=13, textvariable=percentage_weight_finer_two)
percentage_weight_finer_two_entry.grid(column=7, row=2)

percentage_weight_finer_three = tk.DoubleVar()
percentage_weight_finer_three_entry = ttk.Entry(window, width=13, textvariable=percentage_weight_finer_three)
percentage_weight_finer_three_entry.grid(column=7, row=3)

percentage_weight_finer_four = tk.DoubleVar()
percentage_weight_finer_four_entry = ttk.Entry(window, width=13, textvariable=percentage_weight_finer_four)
percentage_weight_finer_four_entry.grid(column=7, row=4)

percentage_weight_finer_five = tk.DoubleVar()
percentage_weight_finer_five_entry = ttk.Entry(window, width=13, textvariable=percentage_weight_finer_five)
percentage_weight_finer_five_entry.grid(column=7, row=5)

percentage_weight_finer_six = tk.DoubleVar()
percentage_weight_finer_six_entry = ttk.Entry(window, width=13, textvariable=percentage_weight_finer_six)
percentage_weight_finer_six_entry.grid(column=7, row=6)

percentage_weight_finer_seven = tk.DoubleVar()
percentage_weight_finer_seven_entry = ttk.Entry(window, width=13, textvariable=percentage_weight_finer_seven)
percentage_weight_finer_seven_entry.grid(column=7, row=7)

percentage_weight_finer_bottom_pan = tk.DoubleVar()
percentage_weight_finer_bottom_pan_entry = ttk.Entry(window, width=13, textvariable=percentage_weight_finer_bottom_pan)
percentage_weight_finer_bottom_pan_entry.grid(column=7, row=8)

percent_wt_finer = ttk.Button(window, text="Calculate", command=cal_percent_wt_finer)
percent_wt_finer.grid(column=7, row=9)

interpretation_col = ttk.Label(window, text="Summary of the soil tested on the basis of the Uniformity Coefficient(Cu)")
interpretation_col.grid(row=11, column=0, columnspan=10)

interpretation_box = scrolledtext.ScrolledText(window, width=64, height=12)
interpretation_box.grid(column=0, row=12, columnspan=10, rowspan=10)

window.mainloop()
