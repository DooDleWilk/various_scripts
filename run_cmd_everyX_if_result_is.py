import subprocess as sp, sys

retry = True
phrase_to_check = "Connection timed out"

while retry:
    try:
        complete = sp.run('ls -l', shell=True,
            stdout = sp.PIPE, stderr = sp.PIPE,
            universal_newlines=True)
        complete.check_returncode()
        retry = False
        for line in complete.stdout.split('\n'):
            print(line)
            if phrase_to_check in line:
                retry = True
        for err in complete.stderr.split('\n'):
            print(err)
            if phrase_to_check in err:
                retry = True
    except sp.SubprocessError as spe:
        print('Execution failed: {}'.format(spe),
              file=sys.stderr)

    sleep(600)

print('Done')

