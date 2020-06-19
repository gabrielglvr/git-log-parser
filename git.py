import os

class GitFile():

    def __init__(self, hashcode, filename):
        self.hashcode = hashcode
        self.filename = filename


###################################################
#                                                 #
#           EDITE AS VARIAVEIS ABAIXO             #
#                                                 #
###################################################

# Jan / Feb / Mar / Apr / May / Jun / Jul / Aug / Sep / Oct / Nov / Dec
initial_date = 'MAY 1 2020'
end_date = 'JUN 30 2020'

# Autor do commit
git_author = ''

# url do projeto SEM O / NO FINAL
project_path = ''


##################################################
#                                                #
#                                                #
#                                                #
##################################################

file_name = 'tmp.git.log'
blob_path = '/-/blob/'
command = f'git --no-pager log --since "{initial_date}" --until "{end_date}" --name-status --author="{git_author}" > {file_name}'

os.system(command)

hashes = dict()
files = list()
    
with open(file_name, 'rt') as file:
    
    file_contents = file
    index = -1
    
    for line in file_contents:

        if("commit " in line):
            index += 1
            commit_hash = line[7:].strip()
            hashes[index] = commit_hash

        if('\t' in line):
            filename = line[2:].strip()
            files.append(GitFile(hashes[index], filename))

commits_filename = f'{git_author}_{initial_date}_{end_date}_commits.txt'

with open(commits_filename, "a") as cf:
    for f in files:
        cf.write(f'{project_path}{blob_path}{f.hashcode}/{f.filename}\n')

os.remove(file_name)

print("#####################################################################################################################################")
print("\n")
print(f'Foram realizados {len(files)} commits no periodo de {initial_date} a {end_date}')
print("\n")
print(f'Foi salvo um arquivo com na pasta raiz do projeto com o nome: {commits_filename}')
print("\n")
print("#####################################################################################################################################")
