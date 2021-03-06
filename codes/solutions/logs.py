# import system function
from datetime import datetime
from operator import itemgetter

# import from project functions
import initial as init


def log_text_add(log_data, log_file_path):
    with open(log_file_path, 'a+') as wf:
        string_to_write = list()
        string_to_write.append(f'\n[Running date and time]\n"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"\n')
        string_to_write.append(f'\n[Config Information]')
        for pair in log_data.items():
            string_to_write.append(f'\n  {pair}"')
        string_to_write.append(f'\n[Running results]\n')
        wf.writelines(string_to_write)
    wf.close()


# write the solution to file
def write_solution(initial_puzzle, puzzle_map, solution, file_path):
    rows = initial_puzzle[0][0]
    cols = initial_puzzle[0][1]

    initial_bulb = []

    for i in range(0, rows):
        for j in range(0, cols):
            if puzzle_map[i][j] == init.CELL_BULB:
                initial_bulb.append([i, j])

    for i in range(0, len(solution)):
        total_bulb = initial_bulb + solution[i].get("bulbs")
        total_bulb.sort()
        first_subfitness = solution[i].get('white_cells') - solution[i].get('empty_cells')
        second_subfitness = solution[i].get('shining_conflict')
        third_subfitness = solution[i].get('black_conflict')

        with open(file_path, 'a+') as wf:
            wf.write(f'\n{first_subfitness}    {second_subfitness}    {third_subfitness}    {i + 1}\n')
            for j in range(0, len(total_bulb)):
                wf.write(f'{total_bulb[j][1] + 1} {total_bulb[j][0] + 1}\n')
        wf.close()


# write the solution to file
def write_solution_four(initial_puzzle, puzzle_map, solution, config):
    rows = initial_puzzle[0][0]
    cols = initial_puzzle[0][1]
    file_path = config["solution_file"]

    initial_bulb = []

    for i in range(0, rows):
        for j in range(0, cols):
            if puzzle_map[i][j] == init.CELL_BULB:
                initial_bulb.append([i, j])

    for i in range(0, len(solution)):
        total_bulb = initial_bulb + solution[i].get("bulbs")
        total_bulb.sort()
        first_subfitness = solution[i].get('white_cells') - solution[i].get('empty_cells')
        second_subfitness = solution[i].get('shining_conflict')
        third_subfitness = solution[i].get('black_conflict')
        if config["number_objectives"] == 4:
            fourth_subfitness = solution[i].get('bulb_cells_total')

        with open(file_path, 'a+') as wf:
            if config["number_objectives"] == 4:
                wf.write(f'\n{first_subfitness}    {second_subfitness}'
                         f'    {third_subfitness}    {fourth_subfitness}'
                         f'    {i + 1}\n')
            else:
                wf.write(f'\n{first_subfitness}    {second_subfitness}'
                         f'    {third_subfitness}'
                         f'    {i + 1}\n')

            for j in range(0, len(total_bulb)):
                wf.write(f'{total_bulb[j][1] + 1} {total_bulb[j][0] + 1}\n')
        wf.close()


# write logs
def logs_write(log_file_path, runs, run_log):
    with open(log_file_path, 'a+') as wf:
        wf.write(f"\nrun {runs + 1} \n")
        for i in range(0, len(run_log)):
            wf.write(f'{str(run_log[i][0]).ljust(6, " ")}'
                     f'   {str(format(run_log[i][1][0], "0.2f")).ljust(6, " ")} '
                     f'   {str(run_log[i][1][1])} '
                     f'   {str(format(run_log[i][1][2], "0.2f")).ljust(5, " ")} '
                     f'   {str(run_log[i][1][3])} '
                     f'   {str(format(run_log[i][1][4], "0.2f")).ljust(5, " ")} '
                     f'   {str(run_log[i][1][5])} \n'
                     )
    wf.close()


# write logs for four objectives
def logs_write_four(config, runs, run_log):
    log_file_path = config["log_file"]
    with open(log_file_path, 'a+') as wf:
        wf.write(f"\nrun {runs + 1} \n")
        for i in range(0, len(run_log)):
            if config["number_objectives"] == 4:
                wf.write(f'{str(run_log[i][0]).ljust(6, " ")}'
                         f'   {str(format(run_log[i][1][0], "0.2f")).ljust(6, " ")} '
                         f'   {str(run_log[i][1][1])} '
                         f'   {str(format(run_log[i][1][2], "0.2f")).ljust(5, " ")} '
                         f'   {str(run_log[i][1][3])} '
                         f'   {str(format(run_log[i][1][4], "0.2f")).ljust(5, " ")} '
                         f'   {str(run_log[i][1][5])} '
                         f'   {str(format(run_log[i][1][6], "0.2f")).ljust(5, " ")} '
                         f'   {str(run_log[i][1][7])} \n'
                         )
            else:
                wf.write(f'{str(run_log[i][0]).ljust(6, " ")}'
                         f'   {str(format(run_log[i][1][0], "0.2f")).ljust(6, " ")} '
                         f'   {str(run_log[i][1][1])} '
                         f'   {str(format(run_log[i][1][2], "0.2f")).ljust(5, " ")} '
                         f'   {str(run_log[i][1][3])} '
                         f'   {str(format(run_log[i][1][4], "0.2f")).ljust(5, " ")} '
                         f'   {str(run_log[i][1][5])} \n'
                         )

    wf.close()
