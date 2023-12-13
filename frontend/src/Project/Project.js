import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import "./Project.css";
import ViewProject from "../ViewProject/ViewProject";
import UpdateProject from "../UpdateProject/UpdateProject";

function Project() {
	const { id } = useParams();
	const URL = `http://127.0.0.1:5000/projects/${id}`;
	const [project, setProject] = useState({
		created_at: "",
		id: 0,
		link: "",
		name: "",
		notes: "",
	});
	const [editMode, setEditMode] = useState(false);
	const [trigger, setTrigger] = useState(false);

	useEffect(() => {
		try {
			fetch(URL, {
				mode: "cors",
			})
				.then((res) => {
					if (!res.ok) {
						throw new Error("HTTP error: ", res.status);
					}
					return res.json();
				})
				.then((data) =>
					setProject({
						created_at: data.created_at,
						id: data.id,
						link: data.link,
						name: data.name,
						notes: data.notes,
					})
				)
				.catch((error) => console.error("Fetch error:", error));
		} catch (error) {
			console.log(error);
		}
	}, [trigger]);

	const onProjectUpdate = () => {
		setEditMode(false);
		setTrigger(!trigger);
	};

	if (editMode === false) {
		return (
			<ViewProject
				project={project}
				setEditMode={setEditMode}
				URL={URL}
			/>
		);
	} else {
		return (
			<UpdateProject
				project={project}
				setEditMode={setEditMode}
				useState={useState}
				id={id}
				projectUpdate={onProjectUpdate}
			/>
		);
	}
}

export default Project;
