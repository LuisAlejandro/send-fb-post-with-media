<p align='center'>
  <img src="https://github.com/LuisAlejandro/send-fb-post-with-media/blob/develop/branding/banner.svg">
  <h3 align="center">Send Facebook post with media</h3>
  <p align="center">GitHub Action for sending a Facebook post with an image</p>
</p>

---

Current version: 0.1.0

## 🎒 Prep Work

1. Get a facebook permanent access token (explained below) using a facebook account that owns the page where you want to post messages.
2. Find the ID of the page that you want to post messages in (explained below).
2. Upload your images to a public access URL.

## 🖥 Workflow Usage

Configure your workflow to use `LuisAlejandro/send-fb-post-with-media@0.1.0`,
and provide the text you want to send as the `STATUS_TEXT` env variable.

You can add up to 4 images as URLs in `STATUS_IMAGE_URL_1`,
`STATUS_IMAGE_URL_2`, `STATUS_IMAGE_URL_3` and `STATUS_IMAGE_URL_4`
env variables. The script will download and attach them to the post.
You can omit all 4 variables and no image will be attached.

Provide the access token for your Facebook app as the
`FACEBOOK_ACCESS_TOKEN` env variable, set your facebook page ID as
`FACEBOOK_PAGE_ID` (as secrets). Remember, to add secrets go to your repository
`Settings` > `Secrets` > `Actions` > `New repository secret`
for each secret.

For example, create a file `.github/workflows/push.yml` on
a github repository with the following content:

```yml
name: Send a Facebook post
on: [push]
jobs:
  post:
    runs-on: ubuntu-20.04
    steps:
      - uses: LuisAlejandro/send-fb-post-with-media@0.1.0
        env:
          FACEBOOK_ACCESS_TOKEN: ${{ secrets.FACEBOOK_ACCESS_TOKEN }}
          FACEBOOK_PAGE_ID: ${{ secrets.FACEBOOK_PAGE_ID }}
          STATUS_TEXT: "Hi! I'm posting from Github actions using https://github.com/LuisAlejandro/send-fb-post-with-media"
          STATUS_IMAGE_URL_1: https://picsum.photos/1024/768
```

Publish your changes, activate your actions if disabled and enjoy.

## 🕵🏾 Hacking suggestions

- You can test the script locally with Docker Compose:

  * Install [Docker Community Edition](https://docs.docker.com/install/#supported-platforms) according with your operating system
  * Install [Docker Compose](https://docs.docker.com/compose/install/) according with your operating system.

      - [Linux](https://docs.docker.com/compose/install/#install-compose-on-linux-systems)
      - [Mac](https://docs.docker.com/compose/install/#install-compose-on-macos)
      - [Windows](https://docs.docker.com/compose/install/#install-compose-on-windows-desktop-systems)

  * Install a git client.
  * Fork this repo.
  * Clone your fork of the repository into your local computer.
  * Open a terminal and navigate to the newly created folder.
  * Change to the `develop` branch.

          git checkout develop

  * Create a `.env` file with the content of the environment secrets as variables, like this (with real values):

          STATUS_TEXT=xxxx
          STATUS_IMAGE_URL_1=xxxx
          STATUS_IMAGE_URL_2=xxxx
          STATUS_IMAGE_URL_3=xxxx
          STATUS_IMAGE_URL_4=xxxx
          FACEBOOK_ACCESS_TOKEN=xxxx
          FACEBOOK_PAGE_ID=xxxx

  * Execute the following command to create the docker image (first time only):

          make image

  * You can execute the publish script with this command:

          make publish

  * Or, alternatively, open a console where you can manually execute the script and debug any errors:

          make console
          python3 entrypoint.py

  * You can stop the docker container with:
  
          make stop

  * Or, destroy it completely:
  
          make destroy
  

## Made with :heart: and :hamburger:

![Banner](https://github.com/LuisAlejandro/send-fb-post-with-media/blob/develop/branding/author-banner.svg)

> Web [luisalejandro.org](http://luisalejandro.org/) · GitHub [@LuisAlejandro](https://github.com/LuisAlejandro) · Twitter [@LuisAlejandro](https://twitter.com/LuisAlejandro)