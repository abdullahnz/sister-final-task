import { useEffect, useState } from "react";
import "./App.css";
import { FileUploader } from "react-drag-drop-files";
import FileInfo from "./components/FileInfo";
import FileStatus from "./components/FileStatus";
import Table from "./components/Table";
import ZipCracker from "./services/api";
import useSessionStorage from "./hooks/useSessionStorage";

const fileTypes = ["ZIP"];

function App() {
  const [file, setFile] = useState(null);
  const [files, setFiles] = useSessionStorage("files", []);

  const fetchAllStatus = async () => {
    files.forEach(async (file) => {
      if (file.status === 0) {
        const resp = await ZipCracker.getStatus(file.taskId);

        if (resp?.status === "SUCCESS") {
          const updatedFiles = files.map((file) => {
            if (file.taskId === resp.task_id) {
              return { ...file, status: 1, result: resp.result };
            }
            return file;
          });
          setFiles(updatedFiles);
        }
      }
    });
  };

  useEffect(() => {
    const interval = setInterval(async () => {
      if (files.length === 0) return;

      fetchAllStatus();
    }, 1000);

    return () => clearInterval(interval);
  });

  const handleChange = (file) => {
    setFile(file);
  };

  const handleAddFile = async () => {
    if (!file) return;

    const resp = await ZipCracker.crack(file);
    const data = { file: file, name: file.name, taskId: resp.task_id, status: 0, result: null };

    setFiles([...files, data]);
    setFile(null);
  };

  const clearSession = () => {
    setFiles([]);
  };

  return (
    <div className="container mt-5">
      <h1 className="text-center mb-5">Parallel Zip Cracker (with 16million++ wordlists)</h1>

      <FileUploader
        handleChange={handleChange}
        name="file"
        types={fileTypes}
        multiple={false}
        classes="min-w-100"
      />

      <FileInfo file={file} />

      <div className="d-flex justify-content-end gap-2">
        <button className="btn btn-primary" onClick={clearSession}>
          Clear session
        </button>
        <button className="btn btn-primary" onClick={handleAddFile}>
          Add file
        </button>
      </div>

      <Table
        title={"Cracking Status"}
        columns={["No", "Filename", "Status", "Password (revealed :v)"]}
      >
        {files.map((data, index) => (
          <FileStatus index={index} data={data} key={index} />
        ))}
      </Table>
    </div>
  );
}

export default App;
