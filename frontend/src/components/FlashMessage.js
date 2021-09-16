import { connect } from 'react-redux';
import { hideFlashMessage } from '../actions';

function FlashMessage({ message, showFlashMessage, hideFlashMessage }) {
  const renderFlashMessage = () => {
    return showFlashMessage ? (
      <ul
        className={`alert-${message.class} alert alert-dismissible fade show text-center`}
        role="alert"
      >
        <div>
          {message.content}
          <button
            type="button"
            className="btn-close"
            onClick={() => hideFlashMessage()}
          />
        </div>
      </ul>
    ) : null;
  };

  if (!message) {
    return null;
  }

  return <div>{renderFlashMessage()}</div>;
}

const mapStateToProps = (state) => {
  return {
    message: state.flashMessage,
    showFlashMessage: state.showFlashMessage,
  };
};

export default connect(mapStateToProps, { hideFlashMessage })(FlashMessage);
