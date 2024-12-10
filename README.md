Dec 08, 2024

The milestone images are stored in [here](./milestones/)

Milestone 1:
- Run `docker-compose up --build` to build and start the services
- Run `docker ps` to check the running services

Milestone 2:
- Run `poetry poe run-feature-engineering-pipeline` will run the feature pipeline which will store the processed data to mongodb


Some problems:
- I encountered BSON document too larget error which prevent me to put all content of the 4 subdomains to MongoDB ([evidence](./milestones/BSON_document_error.jpg))
