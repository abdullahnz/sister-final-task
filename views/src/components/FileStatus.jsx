const FileStatus = ({ index, data }) => {
  return (
    <tr key={index}>
      <th scope="row">{index + 1}</th>
      <td>{data.name}</td>
      <td>
        {data.status === 0 ? (
          <div className="badge bg-primary">processing</div>
        ) : (
          <div className="badge bg-success">done</div>
        )}
      </td>
      <td>
        {data.status === 0 ? (
          <>
            <span
              className="spinner-border spinner-border-sm text-primary me-2"
              role="status"
              aria-hidden="true"
            ></span>
            <span className="sr-only">cracking...</span>
          </>
        ) : (
          <span className="">{data.result ? data.result : "Password not found"}</span>
        )}
      </td>
    </tr>
  );
};

export default FileStatus;
