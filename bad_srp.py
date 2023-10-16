






    def parse_response(self):
        response = self.get_repos_by_user()
        body = response['body']
        if response['status_code'] == 200:
            for i in range(len(body)):
                print(f'{body[i]["id"]} - {body[i]["name"]} - {body[i]["stargazers_count"]}')


repos = ListRepositories('jhooGs')
repos.parse_response()
