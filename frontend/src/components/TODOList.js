const TODOItem = ({TODO}) => {
    return (
        <tr>
            <td>
                {TODO.project_name.name}
            </td>
            <td>
                {TODO.description}
            </td>
        </tr>
    )
}

const TODOList = ({TODOs}) => {
    return (
        <table>
            <th>
                Project Name
            </th>
            <th>
                Description
            </th>

            {TODOs.map((TODO) => <TODOItem TODO={TODO}/>)}
        </table>
    )
}

export default TODOList
