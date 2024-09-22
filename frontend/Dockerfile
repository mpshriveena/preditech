FROM node:18 AS frontend
WORKDIR /preditech/frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend/ .
EXPOSE 5173
CMD ["npm", "run", "dev"]