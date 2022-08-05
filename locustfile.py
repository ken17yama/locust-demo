from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
		# between(min_wait, max_wait): トラフィック投入後にmin_wait~max_waitの範囲でwaitを入れる
		# constant(wait_time): トラフィック投入後に固定の秒数でwaitを入れる
		# constant_pacing(wait_time): トラフィック投入後、wait_time に合う時間分 wait を入れる。安定して負荷をかけたい場合はこの設定
    wait_time = constant(1)

    @task
    def get_contents(self):
        self.client.get("/")
