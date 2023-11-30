import Table from "./Table";

const FileInfo = ({ file }) => {
  return (
    <Table title="File Info" columns={["Filename", "Size", "Type"]}>
      <tr>
        <td>{file ? file.name : "-"}</td>
        <td>{file ? file.size : "-"}</td>
        <td>{file ? file.type : "-"}</td>
      </tr>
    </Table>
  );
};

export default FileInfo;
