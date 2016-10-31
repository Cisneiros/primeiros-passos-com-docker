FROM node:6

ADD . /app

RUN cd /app; npm install --production

EXPOSE 3000

CMD ["node", "/app/index.js"]
