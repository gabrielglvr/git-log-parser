
import os
import sys
class GitFile():
    def __init__(self, hashcode, filename):
        self.hashcode = hashcode
        self.filename = filename
def dir_list(folder ):
    filenames= os.listdir (folder) 
    result = []
    for filename in filenames: 
        if os.path.isdir(os.path.join(os.path.abspath("."), filename)): 
            if not filename.startswith('.'):
                result.append(filename)
    return result
def get_url(folder ):
    try:
        with open(folder + "/.git/config", 'r') as f:
            for line in f:
                if "url" in line:
                    url = line.split()
                    return url[2].replace(" ","")
    except BaseException as identifier:
        return ""

total = 0 
sumario =""
sumario += f'Commits \t'
sumario += f'Repositorio \n'
###################################################
#                                                 #
#           EDITE AS VARIAVEIS ABAIXO             #
#                                                 #
###################################################

# Jan / Feb / Mar / Apr / May / Jun / Jul / Aug / Sep / Oct / Nov / Dec
initial_date = 'MAY 26 2020'
end_date = 'JUN 26 2020'

# Autor do commit
git_author = 'seu usario de comm'


##################################################
#                                                #
#                                                #
#                                                #
##################################################



commits_filename = f'{git_author}_{initial_date}_{end_date}_commits.txt'
file_name = 'tmp.git.log'
blob_path = '/-/blob/'

folder_list = dir_list('.')
print("#################################################################")    
print( "Repositórios git")
print("#################################################################") 
for gitdir in folder_list:
    print( "{}".format(gitdir))
    
    ## retorna a ulr do projeto
    project_path = get_url(gitdir) 
    if len( project_path ) == 0 :
        continue

    command = f'git -C "{gitdir}" --no-pager log --since "{initial_date}" --until "{end_date}" --name-status --author="{git_author}" > {gitdir}.txt'

    os.system(command)
    
    hashes = dict()
    files = list()
    
    with open(gitdir+".txt", 'rt') as file:
        
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

    files.sort(key=lambda x: x.filename, reverse=True)

    with open(commits_filename, "a") as cf:
        for f in files:
            cf.write(f'{project_path}{blob_path}{f.hashcode}/{f.filename}\n')

    os.remove(gitdir+".txt")

    if len(files) > 0:
        sumario += f'{len(files)}'
        sumario += f' \t \t {gitdir} \n'
    total +=len(files)

print("#################################################################")
print("\n")
print(sumario)
print(f'Foram realizados {total} commits no periodo de {initial_date} a {end_date}')
print("\n")
print("#################################################################")
