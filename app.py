import getopt
import json
import os
import requests
import sys

url = ''
gid = ''
token = ''

def setup( argv ):
    '''
    Process the required parameters.
    '''
    global url, gid, token
    try:
        opts, args = getopt.getopt( argv, "u:g:t:", ["url=","gid=", "token="] )
    except getopt.GetoptError:        
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print( 'app.py -u <repository-url> -g <group-id> -t <personal-aceess-token>' )
            sys.exit()
        elif opt in ("-u", "--url"):
            url = arg
        elif opt in ("-g", "--gid"):
            gid = arg
        elif opt in ("-t", "--token"):
            token = arg

def clone():
    '''
    Clone GitLab projects under a given group. This will replicate the
    path of the repositories in your local filesystem.
    '''
    global url, gid, token
    # Get the current working directory
    cwd = os.getcwd()
    print( f'{url}/{gid}/' )
   
    x = requests.get( f'{url}/{gid}', 
                      headers = {"PRIVATE-TOKEN": token} )

    response = json.loads( x.content )
    project_list = response['projects']
    for project in project_list:
        clone = project['ssh_url_to_repo']
        folder_path = os.path.dirname( (clone.split(":")[1]) )
        os.makedirs( f'{cwd}/{folder_path}', exist_ok=True )
        print( f'Changing to{cwd}/{folder_path}' )
        os.chdir( f'{cwd}/{folder_path}' )
        os.system( f'git clone {clone}' )

if __name__ == "__main__":
    setup( sys.argv[1:] )
    clone()


