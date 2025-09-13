# ai-data-anonymiser
Giga hack 2025 (ft Cook M. Bunescu)

## Running with Docker Compose

To start the application using Docker Compose:

1. **Ensure Docker and Docker Compose are installed**  
   On Linux, you can check with:
   ```sh
   docker --version
   docker compose version
   ```

2. **Build and start the services**  
   From the project root directory, run:
   ```sh
   docker compose up -d --build
   ```

3. **Access the services**
   - **Open WebUI:** [http://localhost:3000](http://localhost:3000)
   - **Backend API:** [http://localhost:4605/v1/models](http://localhost:4605/v1/models)

4. **Stop the services**
   ```sh
   docker compose down
   ```