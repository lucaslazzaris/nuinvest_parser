import { shallow } from 'enzyme';
import NotFound from './NotFound';

test('Renders NotFound Component', () => {
  const wrapper = shallow(<NotFound />);
  expect(
    wrapper.contains(
      <h1 className="text-center"> Erro 404: Página não encontrada</h1>
    )
  ).toBeTruthy();
});
