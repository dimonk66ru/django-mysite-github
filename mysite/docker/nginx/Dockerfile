FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
COPY mysite/docker/nginx/nginx.conf /etc/nginx/conf.d
COPY mysite/docker/nginx/proxy_params /etc/nginx