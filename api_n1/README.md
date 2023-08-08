# MountainPeak API

This guide assumes that you are using a linux system.
The MountainPeak is based on a FastAPI, postgreSql python stack.

## Build and run the application

1. Make sure Docker and docker-compose is installed on your system

2. Download this repository.
3. 
        git clone https://github.com/julienCozo/mpeak.git && cd mpeak

3. On the command line you can build the image and start the container:

        docker-compose up --build


4. Open http://localhost:8000/ in your browser.
    You should be greated by a welcome message


## Playing with API

FastAPI include powerfull tool to test API.
Let use Swagger UI which is available at  http://localhost:8000/docs/

Here a list of implemented routes with examples

List all peak with classic pagination implemented (skip and limit)
   * http://localhost:8000/peaks?limit=100

List peak in a bouncing box with query params max_lat min_lat max_lon min_lon
   * http://localhost:8000/boucing_peaks?min_lat=10.1&max_lat=20.1&min_lon=32.1&max_lon=36.8

Read a peak (GET)
   * http://localhost:8000/peak/read/{id}

Update a peak (PUT)
   * http://localhost:8000/peak/update{id}

Delete a Peak (DELETE)
   * http://localhost:8000/peak/delete{id}

Create a peak (POST)
   * http://localhost:8000/peak


Peak schema is 
{
  "name": "string",
  "lat": 0,
  "lon": 0,
  "altitude": 0,
  "id": 0
}

Create schema is
{
  "name": "string",
  "lat": 0,
  "lon": 0,
  "altitude": 0
}



