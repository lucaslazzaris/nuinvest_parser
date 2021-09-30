import { mountWithRouter } from '../helpers/testHelper';
import { shallow } from 'enzyme';
import App from './App';
import TopBar from './TopBar';
import Footer from './Footer';
import Home from './Home';
import About from './About';
// import axiosMock from "axios";

describe('App', () => {
  test('Renders Top Bar', () => {
    const wrapper = shallow(<App />);

    expect(wrapper.find(TopBar)).toHaveLength(1);
  });

  test('Renders Footer', () => {
    const wrapper = shallow(<App />);

    expect(wrapper.find(Footer)).toHaveLength(1);
  });

  test('Renders Home', () => {
    const wrapper = mountWithRouter(<App />);

    expect(wrapper.find(Home)).toHaveLength(1);
  });

  test('Renders About', () => {
    const wrapper = mountWithRouter(<App />, { route: '/sobre' });

    expect(wrapper.find(About)).toHaveLength(1);
  });
});
