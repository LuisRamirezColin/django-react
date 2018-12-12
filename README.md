## Docker compose template
### Includes
* backend  services providing by django 1.11 and python 2.7
* frontend services providing by react 16.6 and ES6

### Requirments
* https://docs.docker.com/compose/overview/
* 

### How to use
Create new folder project
```sh
mkdir project_name
```

Clone docker template
```sh
git clone 
```

## Running

1. `docker-compose build`
2. `docker-compose up`
3. There should now be two servers running:
  - [http://127.0.0.1:8000](http://127.0.0.1:8000) is the Django app
  - [http://127.0.0.1:3000](http://127.0.0.1:3000) is the React app

## Using `docker-compose run` to issue one-off commands

If you want to run a one-off command, like installing dependencies, you can use the `docker-compose run <service_name> <cmd>`.

For example, to install a Javascript dependency and save that information to `package.json` we could run:
`docker-compose run --rm frontend npm install --save axios`

If you want to be on a shell for one of the Docker services, you can do something like:
`docker-compose run --rm frontend bash`

Done.
