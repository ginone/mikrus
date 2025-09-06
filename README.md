# mikrus
Fun projects for mikr.us VPS

* [mikrus config](#mikrus-config)
  * [Install docker](#install-docker)
  * [Install rsync](#install-rsync)
  * [Install pip](#install-pip)
  * [Install pipx](#install-pipx)
  * [Install poetry](#install-poetry)
* [Projects config](#projects-config)
  * [Upload projects to mikr.us (scp)](#upload-projects-to-mikrus-scp)
  * [Upload projects to mikr.us (rsync)](#upload-projects-to-mikrus-rsync)
  * [Append job to crontab](#append-job-to-crontab)


## mikrus config

### Install docker
```bash
apk update \
&& apk add docker \
&& rc-update add docker docker-compose \
&& service docker start
```

### Install rsync
```bash
sudo apk add rsync
```

### Install pip
```bash
sudo apk add py3-pip
```

### Install pipx
```bash
python3 -m pip install --user pipx --break-system-packages \
&& python3 -m pipx ensurepath
```

### Install poetry
```bash
pipx install poetry \
&& poetry config virtualenvs.in-project true
```

## Projects config

### Upload projects to mikr.us (scp)
```bash
scp -P 10617 -r ./maciek frog@frog03.mikr.us:/home/frog
```

### Upload projects to mikr.us (rsync)
```bash
rsync -avz --exclude='.venv' -e "ssh -p 10617" ./maciek frog@frog03.mikr.us:/home/frog
```

### Append job to crontab
```bash
(crontab -l; echo '0 * * * * source /home/frog/.bashrc && cd /home/frog/maciek && poetry run python maciek.py &>> logs.txt') | crontab -
```
