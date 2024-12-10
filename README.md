Dec 08, 2024

### This project is imported from the [LLM-Engineers-Handbook](https://github.com/PacktPublishing/LLM-Engineers-Handbook), please ignore redundant modules which will be used for future development.

The milestone images are stored in [here](./milestones/)

Milestone 1:
- Run `docker-compose up --build` to build and start the services
- Run `docker ps` to check the running services
You can find the docker-compose [here](./docker-compose.yml)

Milestone 2:
- Run `poetry poe run-motion-planning-subdomain` to crawl data from movit2
- Run `poetry poe run-navigation-subdomain` to crawl data from nav2
- Run `poetry poe run-robotics-middleware-subdomain` to crawl data from ros2
- Run `poetry poe run-simulation-subdomain` to crawl data from gazebo
- Run `poetry poe run-feature-engineering-pipeline` will run the feature pipeline which will store the processed data to mongodb


Some problems:
- I encountered BSON document too larget error which prevent me to put all content of the 4 subdomains to MongoDB ([evidence](./milestones/BSON_document_error.jpg))

