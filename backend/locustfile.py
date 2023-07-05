from locust import HttpUser, between, SequentialTaskSet, task


class UserBehavior(SequentialTaskSet):

    @task
    def put_settings(self):
        headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
        data = {
            "id": "0",
            "note": False,
            "task": True,
            "reminder": True,
            "email": True,
            "push": True,
            "user_id": "1"
        }
        self.client.put("/settings", params={"authorization": "1234567lalalala"}, headers=headers, json=data)

    @task
    def get_settings(self):
        self.client.get("/settings", params={"user_id": 1, "authorization": "1234567lalalala"})

    @task
    def post_note(self):
        headers = {'accept': 'application/json', 'Content-Type': 'application/json', 'user_id': '1'}
        data = {
            "content": "this is 1 note"
        }
        self.client.post("/notes", params={"authorization": "1234567lalalala"}, headers=headers, json=data)


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 2.5)
