Hopefully this saves you 30 minutes next time you want to start a flask/postgres project.

Bring up as usual: `docker-compose up -d app db`

View logs: `docker-compose logs -f app db`

Visit `http://localhost:5000/add-joe` in your favorite browser (or `curl` a `GET`), then bring up the `User` table in your favorite postgres client. If all goes smoothly, you'll note that a certain `joe@example.com` is present.
