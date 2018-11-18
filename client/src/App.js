import { rgba } from 'polished';
import React, { Component } from 'react';
import styled from 'styled-components';

const AppComponent = styled.div`
	display: flex;
	flex-direction: column;
	width: 35rem;
	margin: 0 auto;
	padding: 6rem 0;
`;

const Form = styled.form`
	display: flex;
	flex-direction: column;
`;

const Label = styled.label`
	display: block;
	font-size: 1.5rem;
	font-weight: 500;
`;

const TextField = styled.textarea`
	margin-top: 0.5rem;
	display: block;
	width: 100%;
	height: 10rem;
	padding: 0.5rem;
	font-size: 1rem;
	border: none;
	resize: none;
	font-family: 'Noto Sans TC', sans-serif;
`;

const WordCount = styled.p`
	font-size: 0.875rem;
	font-weight: 500;
`;

const Button = styled.button`
	align-self: center;
	margin-top: 3rem;
	font-size: 1.25rem;
	font-weight: 600;
	border-radius: 6px;
	padding: 1rem 2rem;
	background: #f5c518;
	box-shadow: 0 5px 15px 0 ${rgba('#f5c518', 0.2)};
	border: none;
	cursor: pointer;
	transition: 0.2s all;
	font-family: 'Noto Sans TC', sans-serif;

	&:active {
		color: black;
	}
`;

const Result = styled.p`
	margin-top: 4rem;
	align-self: center;
	font-size: 2.5rem;
	font-weight: 500;
`;

class App extends Component {
	constructor(props) {
		super(props);

		this.state = {
			storyline: '',
			revenue: null,
			loading: false,
		};

		this.numWords = this.numWords.bind(this);
		this.handleChange = this.handleChange.bind(this);
		this.handleSubmit = this.handleSubmit.bind(this);
	}

	numWords() {
		return this.state.storyline.split(' ').filter(word => word.length > 0)
			.length;
	}

	handleChange(event) {
		const { value } = event.target;

		if (this.numWords() >= 250 && value.length > this.state.storyline.length) {
			return;
		}

		this.setState({
			storyline: value,
		});
	}

	handleSubmit(event) {
		event.preventDefault();

		const { storyline } = this.state;

		this.setState({ loading: true });

		fetch('/get-revenue', {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				storyline,
			}),
		})
			.then(res => res.json())
			.then(json => {
				this.setState({ loading: false, revenue: json.revenue });
			});
	}

	render() {
		return (
			<AppComponent>
				<Form onSubmit={this.handleSubmit}>
					<Label>Storyline</Label>
					<TextField
						name="storyline"
						placeholder="A long time ago in a galaxy far, far away..."
						value={this.state.storyline}
						onChange={this.handleChange}
					/>
					<WordCount>{this.numWords()} / 250</WordCount>
					<Button>Predict revenue</Button>
				</Form>
				<Result>
					{this.state.loading
						? 'Loading...'
						: this.state.revenue && `$${this.state.revenue}`}
				</Result>
			</AppComponent>
		);
	}
}

export default App;
