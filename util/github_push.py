import requests
import git
import datetime

class GithubPush:
    # local_path, token setting needed
    local_path = 'local_path'   #'C:\Mine\kakao-dev-article'
    token = 'token'

    def push_to_github(local_path, token):
        try:
            repo = git.Repo({local_path})
            # repo.remotes[remote_name].pull('main')
            repo.git.add('--all')  # markdown for upload
            repo.index.commit('update markdown ' + str(datetime.date.today()))
            repo.git.push(f'https://{token}@github.com/GDGSongDo/kakao-dev-article.git', f'HEAD:main')
        except Exception as e:
            print(e)
