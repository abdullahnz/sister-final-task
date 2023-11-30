const Table = ({ title, columns, children }) => {
  return (
    <>
      <h3 className="mt-5">{title}</h3>
      <table className="table">
        <thead>
          <tr>
            {columns.map((column, index) => (
              <th key={index} scope="col">
                {column}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>{children}</tbody>
      </table>
    </>
  );
};

export default Table;
