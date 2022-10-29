install `heroku` on ubuntu `sudo snap install heroku --classic` or install heroku CLI `curl https://cli-assets.heroku.com/install.sh | sh`

check install version `heroku --version`

get help `heroku --help`

login heroku `heroku login`

create `runtime.txt` for specify python version python-3.9.15 for heroku detect version python

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key. heroku login create repo on heroku `heroku create`

define how to run your app with Procfile `touch Profile`

connect git with heroku `heroku git:remote -a <your-heroku-app-name>`

commit changes with git

	git add .
	git commit -am "make it better"
	deploy repo on heroku git push heroku main

*Note* python verison 3.6.9 is not supported on heroku
