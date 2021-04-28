Prerequisits:
 - heroku account
 - github account
 - docker
 - python (optional) in case you want to run it without docker

Clone repo:
<pre>
git clone https://github.com/ivasso/kudi-ya-popav
cd kudi-ya-popav
</pre>

Build docker image
<pre>
docker image build -t kudi-ya-popav .
</pre>

run docker image for the first time
<pre>
docker run -it -p 80:8000 --name kudi-ya-popav-app kudi-ya-popav
</pre>

run docker image
<pre>
docker run -it -p 80:8000 kudi-ya-popav
</pre>

Go to browser: http://127.0.0.1


heroku push directly
<pre>
heroku create "name-for-your-app"
heroku container:push web --app "name-for-your-app"
heroku container:release web --app "name-for-your-app"
</pre>
