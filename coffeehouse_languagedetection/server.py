import coffeehouse_languagedetection
from hyper_internal_service import web

__all__ = ['Server']


class Server(object):

    def __init__(self, port=5606):
        """
        Public Constructor
        :param port:
        """
        self.port = port
        self.web_application = web.Application()
        self.web_application.add_routes(
            [web.post('/', self.predict)]
        )

    async def predict(self, request):
        """
        Handles the predict request "/", usage:
        POST:: "input": str
        :param request:
        :return:
        """
        post_data = await request.post()
        algorithm_cld = True
        algorithm_ld = True
        algorithm_dltc = True
        seed = None
        if "cld" in post_data:
            if post_data["cld"] == "0":
                algorithm_cld = False
        if "ld" in post_data:
            if post_data["ld"] == "0":
                algorithm_ld = False
        if "dltc" in post_data:
            if post_data["dltc"] == "0":
                algorithm_dltc = False
        if "seed" in post_data:
            seed = post_data["seed"]
        results = coffeehouse_languagedetection.predict(post_data["input"],
                                                        dltc=algorithm_dltc,
                                                        cld=algorithm_cld,
                                                        ld=algorithm_ld,
                                                        seed=seed,
                                                        as_string=True)
        response = {
            "status": True,
            "results": results
        }
        return web.json_response(response)

    def start(self):
        """
        Starts the web application
        :return:
        """
        web.run_app(app=self.web_application, port=self.port)
        return True

    def stop(self):
        """
        Stops the web application
        :return:
        """
        self.web_application.shutdown()
        self.web_application.cleanup()
        return True
