def vsota_kvadratov_št_1_do_x(x):
    kvadrati_posameznih = []
    for i in range(1, x + 1):
        kvadrati_posameznih.append(i*i)
    return(sum(kvadrati_posameznih))

def kvadrat_vsote_1_do_x(x):
    return sum(range(1, x + 1)) * sum(range(1, x + 1))

def razlika_med_kvadratomvsote_in_vsotekvadratov(x):
    return kvadrat_vsote_1_do_x(x) - vsota_kvadratov_št_1_do_x(x)
