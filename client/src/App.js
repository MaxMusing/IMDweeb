import { rgba } from 'polished';
import React, { Component } from 'react';
import styled from 'styled-components';
import LogoImage from './logo.svg';

const AppComponent = styled.div`
	display: flex;
	flex-direction: column;
	width: 35rem;
	margin: 0 auto;
`;

const Logo = styled.img`
	margin-top: -2rem;
	height: 14rem;
`;

const Description = styled.p`
	font-size: 1rem;
	margin-top: -2rem;
`;

const Form = styled.form`
	margin-top: 3rem;
	display: flex;
	flex-direction: column;
`;

const Label = styled.label`
	display: block;
	font-size: 1.25rem;
	font-weight: 500;
`;

const TextField = styled.textarea`
	margin-top: 0.5rem;
	display: block;
	width: 100%;
	height: 12rem;
	padding: 0.5rem;
	font-size: 1rem;
	border: none;
	resize: none;
	font-family: 'Noto Sans TC', sans-serif;
`;

const WordCount = styled.p`
	margin-top: 0.5rem;
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

const ResultContainer = styled.div`
	margin-top: 4rem;
	text-align: center;
`;

const ResultLabel = styled.p`
	align-self: center;
	font-size: 1.25rem;
	font-weight: 500;
`;

const Result = styled.p`
	align-self: center;
	font-size: 2.5rem;
	font-weight: 500;
`;

class App extends Component {
	constructor(props) {
		super(props);

		this.state = {
			storyline: '',
			genre: null,
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

		fetch('/get-genre', {
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
				this.setState({ loading: false, genre: json.genre });
			});
	}

	render() {
		return (
			<AppComponent>
				<Logo src={LogoImage} />
				<Description>
					IMDweeb uses <strong>natural language processing</strong> and{' '}
					<strong>machine learning</strong> to predict a movie's genre based off
					a short storyline. Enter your idea for the next big movie below!
				</Description>
				<Form onSubmit={this.handleSubmit}>
					<Label>Storyline</Label>
					<TextField
						name="storyline"
						placeholder="A long time ago in a galaxy far, far away..."
						value={this.state.storyline}
						onChange={this.handleChange}
					/>
					<WordCount>{this.numWords()} / 250</WordCount>
					<Button>Predict genre</Button>
				</Form>
				{this.state.loading ? (
					<ResultContainer>
						<Result>Loading</Result>
					</ResultContainer>
				) : (
					this.state.genre && (
						<ResultContainer>
							<ResultLabel>Predicted genre</ResultLabel>
							<Result>{this.state.genre}</Result>
						</ResultContainer>
					)
				)}
			</AppComponent>
		);
	}
}

export default App;
