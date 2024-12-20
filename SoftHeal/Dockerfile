# Use nginx as the base image
FROM nginx:stable-alpine

# Copy static HTML/JS files to the nginx container
COPY . /usr/share/nginx/html

# Expose port 80 to serve the files
EXPOSE 80
