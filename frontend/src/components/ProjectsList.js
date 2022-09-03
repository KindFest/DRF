const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.repo_link}
            </td>
        </tr>
    )
}

const ProjectsList = ({projects}) => {
    return (
        <table>
            <th>
                Project Name
            </th>
            <th>
                Project Link
            </th>

            {projects.map((project) => <ProjectItem project={project}/>)}
        </table>
    )
}

export default ProjectsList
