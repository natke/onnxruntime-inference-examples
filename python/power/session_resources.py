import onnxruntime as ort
import score

def init_resources():
    return score.init()

class SessionResources: # This is a wrapper to make the current InferenceSession class pickleable.
    def __init__(self):
        self.name = "SessionResources"
        self.tokenizer, self.session, self.model, self.device = init_resources()

    def run(self, *args):
        return self.sess.run(*args)

    def __getstate__(self):
        return {'name': self.name}

    def __setstate__(self, values):
        self.tokenizer, self.session, self.model, self.device = init_resources()


