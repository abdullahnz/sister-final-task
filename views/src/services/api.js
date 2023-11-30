import axios from "axios";

class ZipCracker {
  constructor() {
    this.api = axios.create({
      baseURL: "http://localhost:8000",
    });
  }

  crack = (zipFile) => {
    const formData = new FormData();
    formData.append("zip_file", zipFile);

    return this.api
      .post("/zipcrack", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
      .then((response) => {
        return response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  };

  getStatus = (taskId) => {
    return this.api
      .get(`/zipcrack/${taskId}`)
      .then((response) => {
        return response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  };
}

export default new ZipCracker();
