# -------------------------------------------------------------------
#                   BACKEND
# -------------------------------------------------------------------

# Weight of Sample retained formula
def wt_of_sam_ret(emp_sve_sam, wt_of_sv_sam):
    """
    Weight of sample retained is the difference between each Weight of sieve + sample and Weight of empty sieve
    emp_sve_sam = Weight of empty sieve
    wt_of_sv_sam =  Weight of sieve + sample
    """

    result = float(wt_of_sv_sam) - float(emp_sve_sam)
    return float("{0:.2f}".format(result))


# corrected weight of sample retained
def cor_wt_sam_ret(init_sam_wgh, wt_rt_sum):
    """
    corrected weight of sample retained is calculated due to the fact that during shaking or pouring of the sample into
    the sieves, some samples fall on the ground and this amounts to a loss. Corrected weight of sample retained is the
    difference between the initial sample weighed and the sum of the weight of sample retained divided by the number of
    sieves used, added to the eight of sample retained.

    init_sam_wgh = Initial Weight of Sample
    wt_rt_sum = The Sum of Sample retained
    """
    result = (float(init_sam_wgh) - float(wt_rt_sum))/8
    return float("{0:.3f}".format(result))


# percentage weight retained
def percent_wt_ret(cor_wt_of_sam_rt, total_sam_wt_rt):
    """
    the percentage weight is the percentage of the corrected weight of samples retained
    wt_of_sam_rt = corrected weight of samples retained
    total_sam_wt_rt = total weight of sample
    """
    result = float(cor_wt_of_sam_rt)/float(total_sam_wt_rt)*100
    return float("{0:.2f}".format(result))


# cumulative percentage weight retained
def cu_pt_wt_rt(pt_wt_ret_previous, pt_wt_ret_next):
    """
    cumulative percentage finer is sum of percentage retained in each sieve
    pt_wt_ret = percentage weight retained for each sieve
    cu_pt_wt_rt_row = cumulative weight retained for each of above sieve
    """
    result = float(pt_wt_ret_previous) + float(pt_wt_ret_next)
    return float("{0:.2f}".format(result))


# percentage finer
def pt_finer(cu_pt_wt_rt_row):
    """
    percentage finer is percentage difference in each cumulative percentage weight retained
    cu_pt_wt_rt_row = cumulative percentage weight retained per row
    """
    result = 100.01 - float(cu_pt_wt_rt_row)
    return float("{0:.2f}".format(result))

