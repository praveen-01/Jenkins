from flask import Flask,request,jsonify
import time
import token_bucket_rate_limiting

app = Flask(__name__)
user_buckets = {}

def ratelimiter(capacity = 5,refill_rate = 5/60): #5 requests per minute
    def decorator(f):
        def wrapper(*args,**kwargs):
            user_id = request.remote_addr
            print(user_id)

            if user_id not in user_buckets:
                user_buckets[user_id] = token_bucket_rate_limiting.Tokenbucket(capacity, refill_rate)

            bucket = user_buckets[user_id]

            if bucket.allow_request():
                return f(*args, **kwargs)
            else:
                return jsonify({"error": "Rate limit exceeded"}), 429
        wrapper.__name__ = f.__name__
        return wrapper
    return decorator

@app.route("/app/route")
@ratelimiter()
def first_endpoint():
    return jsonify({"hello":"world"}),200

if __name__ == "__main__":
    app.run(debug=True)
