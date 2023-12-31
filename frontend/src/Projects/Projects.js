import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./Projects.css";

function Projects() {
	const URL = "http://127.0.0.1:5000/projects";
	const [projects, setProjects] = useState([]);
	const navigate = useNavigate();

	useEffect(() => {
		fetch(URL, {
			mode: "cors",
		})
			.then((res) => res.json())
			.then((data) => {
				setProjects(data.projects.reverse());
			});
	}, []);

	return (
		<>
			<div className="all-projects-container">
				<h1>All Projects</h1>
				<div className="add-project">
					<button onClick={() => navigate("/add-project")}>
						Add Project
					</button>
				</div>
				<div className="cards-container">
					{projects.map((project) => {
						return (
							<div key={project.id} className="project">
								<h2>{project.name}</h2>
								<a
									href={`http://localhost:3000/projects/${project.id}`}
								>
									<button>View Project</button>
								</a>
							</div>
						);
					})}
				</div>
			</div>
		</>
	);
}

export default Projects;
