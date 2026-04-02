import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const uploadPhotoPromise = uploadPhoto(fileName);
  const signUpUserPromise = signUpUser(firstName, lastName);

  return Promise.allSettled([uploadPhotoPromise, signUpUserPromise]).then((results) => (
    results.map((result) => ({
      status: result.status,
      value: result.status === 'fulfilled' ? result.value : result.reason,
    }))
  ));
}

